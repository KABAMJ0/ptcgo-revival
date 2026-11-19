from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.trainers import team_plasma_card
from ptcgo.game.session.effects import is_pokemon_card, is_trainer_card
from ptcgo.game.card_effects.pokemon import is_energy_card


async def transfer_junk(ctx):
    """One Team Plasma Pokemon, one Team Plasma Trainer and one Team Plasma
    Energy out of the discard pile, each from its own group."""
    groups = (
        ("a Team Plasma Pok\u00e9mon", is_pokemon_card),
        ("a Team Plasma Trainer card", is_trainer_card),
        ("a Team Plasma Energy card", is_energy_card),
    )
    picks = []
    for label, kind in groups:
        pool = [card for card in ctx.discard_pile()
                if team_plasma_card(card) and kind(card)]
        if not pool:
            continue
        picks.extend(await ctx.choose_cards(
            pool, 1, minimum=1,
            prompt="Choose %s to put into your hand" % label))
    if picks:
        await ctx.put_in_hand(picks, reveal=True)

card = PokemonCardDef(
    guid="11a3c887-5149-598d-8666-bbf36100f77a",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name",
    display_name="Raticate",
    searchable_by=["Raticate", "Stage 1", "Team Plasma", "Raticate"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=88,
    set_code="BW9",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    family_id=19,
    abilities=[
        Attack(
            title="Transfer Junk",
            game_text="Put a Team Plasma Pok\u00e9mon, a Team Plasma Trainer card, and a Team Plasma Energy card from your discard pile into your hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=transfer_junk,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
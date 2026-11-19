from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.pokemon import is_energy_card

async def eruption(ctx):
    """Discard the top card of each player's deck; 100 more for each Energy
    discarded this way."""
    discarded = []
    for pid in (ctx.player_id, ctx.opponent_id):
        top = ctx.deck_top(1, pid)
        if top:
            discarded.extend(top)
    if discarded:
        await ctx.discard_cards(discarded)
    energies = sum(1 for c in discarded if is_energy_card(c))
    await ctx.deal_damage(50 + 100 * energies)

card = PokemonCardDef(
    guid="2b0dbfa2-7732-5568-b756-0313cb1b6428",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Camerupt.Name",
    display_name="Camerupt",
    searchable_by=["Camerupt", "Stage 1", "Camerupt"],
    subtypes=["Stage 1"],
    collector_number=32,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name",
    family_id=322,
    abilities=[
        Attack(
            title="Eruption",
            game_text="Discard the top card of each player's deck. This attack does 100 more damage for each Energy card discarded in this way.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=eruption,
        ),
        Attack(
            title="Steaming Stomp",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
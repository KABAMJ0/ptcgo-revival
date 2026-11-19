from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.session.effects import full_stack


async def dust_storm(ctx):
    """Printed 100; then both Active Pokemon and everything attached to them
    are discarded (not a Knock Out, so no Prizes)."""
    await ctx.deal_damage()
    for active in (ctx.opponent_active(), ctx.my_active()):
        if active is not None:
            await ctx.discard_cards(full_stack(active))


card = PokemonCardDef(
    guid="c5910b01-23f0-5b6b-bce6-689daac40dba",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palossand.Name",
    display_name="Palossand",
    searchable_by=["Palossand", "Stage 1", "Palossand"],
    subtypes=["Stage 1"],
    collector_number=62,
    set_code="SM3",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name",
    family_id=769,
    abilities=[
        Attack(
            title="Sand Tomb",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=no_retreat_attack(),
        ),
        Attack(
            title="Dust Storm",
            game_text="Discard all cards from both Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            effect=dust_storm,
        ),
    ],
)
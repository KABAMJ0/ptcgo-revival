from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _heartfelt_song(ctx):
    defender = ctx.defender
    if defender is None or ctx.effects_blocked(defender):
        return
    await ctx.discard_energy_from(
        defender, 1,
        predicate=lambda e: energy_provides_type(e, PokemonTypes.DARKNESS.value),
        prompt="Choose a Darkness Energy to discard")


card = PokemonCardDef(
    guid="001082b4-10d4-5828-a145-064f1ee0e7a4",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name",
    display_name="Jigglypuff",
    searchable_by=["Jigglypuff", "Basic", "Jigglypuff"],
    subtypes=["Basic"],
    collector_number=87,
    set_code="XY1",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    family_id=39,
    abilities=[
        Attack(
            title="Rollout",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Heartfelt Song",
            game_text="Discard a Darkness Energy attached to your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FAIRY: 1},
            effect=_heartfelt_song,
        ),
    ],
)
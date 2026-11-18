from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ab2325c-9dbc-5297-b6f3-f4b12145a2d4",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=97,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Ability(
            title="Here for Hypnosis",
            game_text="When you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon during your turn, you may make your opponent's Active Pok\u00e9mon Asleep.",
            effect=unimplemented,
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
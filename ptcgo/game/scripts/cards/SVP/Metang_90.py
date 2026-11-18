from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c1ac56be-4bf5-5759-8732-4d605dc4aac0",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=90,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    family_id=375,
    abilities=[
        Ability(
            title="Metal Maker",
            game_text="Once during your turn, you may look at the top 4 cards of your deck and attach any number of Basic Metal Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards and put them on the bottom of your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
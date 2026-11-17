from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="c0499e99-e39b-5c6b-8431-dcd4ee8c6b04",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    display_name="Arceus",
    searchable_by=["Arceus", "Basic", "Arceus"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="PL4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=493,
    abilities=[
        Attack(
            title="Metal Barrier",
            game_text="Prevent all effects of attacks, including damage, done to Arceus by Pok\u00e9mon LV.X during your opponent's next turn.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f7a2a775-fbb3-513c-a33e-4b6f600c34a1",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    display_name="Clamperl",
    searchable_by=["Clamperl", "Basic", "Clamperl"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="SM7",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=366,
    abilities=[
        Ability(
            title="Evolutionary Advantage",
            game_text="If you go second, this Pok\u00e9mon can evolve during your first turn.",
            effect=unimplemented,
        ),
        Attack(
            title="Sparkling Pearl",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4b7abd09-5398-5def-955b-6c30e6d46869",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name",
    display_name="Veluza",
    searchable_by=["Veluza", "Basic", "Veluza"],
    subtypes=["Basic"],
    collector_number=125,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=976,
    abilities=[
        Attack(
            title="Ram",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
        Attack(
            title="Slim Screw",
            game_text="If you have no cards in your hand, this attack can be used for Water.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)
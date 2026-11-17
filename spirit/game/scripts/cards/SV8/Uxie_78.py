from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b1e1ff20-9391-552d-957b-eef3f6d70d61",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Uxie.Name",
    display_name="Uxie",
    searchable_by=["Uxie", "Basic", "Uxie"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=480,
    abilities=[
        Attack(
            title="Painful Memories",
            game_text="Put 2 damage counters on each of your opponent's Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)
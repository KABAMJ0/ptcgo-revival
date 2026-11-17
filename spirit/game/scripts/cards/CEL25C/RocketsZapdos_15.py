from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="09030434-2500-5a60-8311-3d798f3a104c",
    key="CEL25C",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RocketsZapdos.Name",
    display_name="Rocket's Zapdos",
    searchable_by=["Rocket's Zapdos", "Basic", "RocketsZapdos"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="CEL25C",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=145,
    abilities=[
        Attack(
            title="Plasma",
            game_text="If there are any Lightning Energy cards in your discard pile, attach 1 of them to Rocket's Zapdos.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Electroburn",
            game_text="Rocket's Zapdos does damage to itself equal to 10 times the number of Lightning Energy cards attached to it.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)
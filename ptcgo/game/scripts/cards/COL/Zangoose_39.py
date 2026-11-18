from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="da1a777f-e942-56da-a07c-fc05a088d4c1",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangoose.Name",
    display_name="Zangoose",
    searchable_by=["Zangoose", "Basic", "Zangoose"],
    subtypes=["Basic"],
    collector_number=39,
    set_code="COL",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Swords Dance",
            game_text="During your next turn, Zangoose's Lost Claw attack's base damage is 80.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Lost Claw",
            game_text="Choose 1 card from your opponent's hand without looking and put it in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
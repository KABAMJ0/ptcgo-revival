from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0dca2680-1156-591a-a0e0-6117fdf672aa",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansPinsir.Name",
    display_name="Ethan's Pinsir",
    searchable_by=["Ethan's Pinsir", "Basic", "EthansPinsir"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="SV10",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    family_id=127,
    abilities=[
        Attack(
            title="Vise Grip",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title="Rallying Horn",
            game_text="If any of your Ethan's Pok\u00e9mon were Knocked Out by damage from an attack during your opponent's last turn, this attack does 100 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
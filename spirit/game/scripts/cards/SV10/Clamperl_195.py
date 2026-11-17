from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="9b8c70d8-416c-51fd-ac07-6379db6df234",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clamperl.Name",
    display_name="Clamperl",
    searchable_by=["Clamperl", "Basic", "Clamperl"],
    subtypes=["Basic"],
    collector_number=195,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=366,
    abilities=[
        Attack(
            title="Shell Press",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 10 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)
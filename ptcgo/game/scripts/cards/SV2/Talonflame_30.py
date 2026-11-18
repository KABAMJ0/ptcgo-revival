from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2b4fb12a-5ab5-5b89-a8ea-9a3648edca13",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflame.Name",
    display_name="Talonflame",
    searchable_by=["Talonflame", "Stage 2", "Talonflame"],
    subtypes=["Stage 2"],
    collector_number=30,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Attack(
            title="Clutch",
            game_text="During your opponent's next turn, the Defending Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIRE: 1},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Fiery Breeze",
            game_text="If this Pok\u00e9mon has any damage counters on it, this attack does 90 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=70,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
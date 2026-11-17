from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95121dab-15a8-52eb-bd82-4d392e4f72c0",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grafaiai.Name",
    display_name="Grafaiai",
    searchable_by=["Grafaiai", "Stage 1", "Grafaiai"],
    subtypes=["Stage 1"],
    collector_number=190,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shroodle.Name",
    family_id=944,
    abilities=[
        Attack(
            title="Spit Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Colorful Graffiti",
            game_text="You may discard as many Basic Energy cards as you like from your hand. This attack does 40 damage for each type of Basic Energy you discarded in this way.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=40,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
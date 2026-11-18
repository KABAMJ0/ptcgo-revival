from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fd618eec-29f8-5ec2-9f5b-ef284ed871e4",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Arbok.Name",
    display_name="Arbok",
    searchable_by=["Arbok", "Stage 1", "Arbok"],
    subtypes=["Stage 1"],
    collector_number=101,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name",
    family_id=23,
    abilities=[
        Attack(
            title="Panic Poison",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned, Confused, and Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Darkness Fang",
            cost={PokemonTypes.DARKNESS: 2},
            damage=70,
        ),
    ],
)
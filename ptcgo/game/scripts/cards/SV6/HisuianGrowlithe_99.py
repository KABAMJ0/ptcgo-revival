from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a71ecd78-b049-55d1-aa87-c15218c9705a",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HisuianGrowlithe.Name",
    display_name="Hisuian Growlithe",
    searchable_by=["Hisuian Growlithe", "Basic", "HisuianGrowlithe"],
    subtypes=["Basic"],
    collector_number=99,
    set_code="SV6",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=58,
    abilities=[
        Attack(
            title="Blazing Destruction",
            game_text="Discard a Stadium in play.",
            cost={},
            effect=unimplemented,
        ),
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=recoil_attack(10),
        ),
    ],
)
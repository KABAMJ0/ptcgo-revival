from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3873c47d-82ae-58c4-96c8-a820b97a0603",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Turtonator.Name",
    display_name="Turtonator",
    searchable_by=["Turtonator", "Basic", "Turtonator"],
    subtypes=["Basic"],
    collector_number=25,
    set_code="SV7",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    family_id=776,
    abilities=[
        Attack(
            title="Ring of Fire",
            game_text="Your opponent's Active Pok\u00e9mon is now Burned. During your opponent's next turn, that Pok\u00e9mon can't retreat.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=unimplemented,
        ),
        Attack(
            title="Inferno Onrush",
            game_text="This Pok\u00e9mon also does 60 damage to itself.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=180,
            effect=recoil_attack(60),
        ),
    ],
)
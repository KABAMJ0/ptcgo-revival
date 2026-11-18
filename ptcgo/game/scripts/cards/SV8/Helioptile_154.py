from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f5e974cd-2436-5536-9758-34965be71e3c",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Helioptile.Name",
    display_name="Helioptile",
    searchable_by=["Helioptile", "Basic", "Helioptile"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="SV8",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=694,
    abilities=[
        Attack(
            title="Tiny Bolt",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pok\u00e9mon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=recoil_attack(10),
        ),
    ],
)
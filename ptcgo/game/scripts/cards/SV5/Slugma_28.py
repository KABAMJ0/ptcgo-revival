from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import condition_bonus_attack
from ptcgo.game.attributes import SpecialConditions

card = PokemonCardDef(
    guid="c11376a1-6ebe-598c-b093-818898404f3b",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    display_name="Slugma",
    searchable_by=["Slugma", "Basic", "Slugma"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SV5",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=218,
    abilities=[
        Attack(
            title="Roasting Heat",
            game_text="If your opponent's Active Pok\u00e9mon is Burned, this attack does 40 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            damage_operator="+",
            effect=condition_bonus_attack(40, SpecialConditions.BURNED, base=10),
        ),
    ],
)
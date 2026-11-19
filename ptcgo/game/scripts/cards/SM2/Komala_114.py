from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import AttrID, CLIENT_SPECIAL_CONDITION_NAMES, SpecialConditions
from ptcgo.game.card_effects.attacks_common import bonus_if


def _is_asleep(ctx) -> bool:
    attacker = ctx.attacker
    return (attacker is not None
            and CLIENT_SPECIAL_CONDITION_NAMES[SpecialConditions.ASLEEP]
            in (attacker.get_attribute(AttrID.SPECIAL_CONDITIONS) or []))


card = PokemonCardDef(
    guid="8525448c-f8df-5c36-9207-5ee60e545408",
    key="SM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Komala.Name",
    display_name="Komala",
    searchable_by=["Komala", "Basic", "Komala"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SM2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=775,
    abilities=[
        Ability(
            title="Comatose",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, whenever you attach an Energy from your hand to it, it is now Asleep.",
            effect=unimplemented,
        ),
        Attack(
            title="Hypno Roll",
            game_text="This attack can be used if this Pok\u00e9mon is Asleep. If it is not Asleep, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
            effect=bonus_if(_is_asleep, 0, else_nothing=True),
            usable_despite_conditions=True,
        ),
    ],
)
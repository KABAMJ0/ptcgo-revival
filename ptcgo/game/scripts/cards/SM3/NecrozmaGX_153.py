from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.attacks_common import discard_for_bonus
from ptcgo.game.card_effects.passives_common import prevent_damage_when
from ptcgo.game.card_effects.pokemon import energy_provides_type, is_energy_card


def _attacker_is_colorless(calc, carrier) -> bool:
    return (calc.target is carrier
            and calc.attacker is not None
            and PokemonTypes.COLORLESS.value
            in (calc.attacker.get_attribute(AttrID.POKEMON_TYPES) or []))


def _is_psychic_energy(card) -> bool:
    return is_energy_card(card) and energy_provides_type(card, PokemonTypes.PSYCHIC.value)

card = PokemonCardDef(
    guid="88ac58b9-eca6-5a88-b4f0-78c6ac200656",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NecrozmaGX.Name",
    display_name="Necrozma-GX",
    searchable_by=["Necrozma-GX", "Basic", "GX", "NecrozmaGX"],
    subtypes=["Basic", "GX"],
    collector_number=153,
    set_code="SM3",
    rarity=Rarities.RareRainbow,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=800,
    abilities=[
        Ability(
            title="Light's End",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from Colorless Pok\u00e9mon.",
            passive=prevent_damage_when(_attacker_is_colorless),
        ),
        Attack(
            title="Prismatic Burst",
            game_text="Discard all Psychic Energy from this Pok\u00e9mon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=10,
            damage_operator="+",
            effect=discard_for_bonus(source="self-energy", predicate=_is_psychic_energy,
                              max_count=99, per=60, optional=False, base=10),
        ),
        Attack(
            title="Black Ray-GX",
            game_text="This attack does 100 damage to each of your opponent's Pok\u00e9mon-GX and Pok\u00e9mon-EX. This damage isn't affected by Weakness or Resistance. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, subtypes_for
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.passives_common import prevent_damage_when


def _is_basic_ex(pokemon) -> bool:
    if pokemon is None:
        return False
    if pokemon.get_attribute(AttrID.STAGE) != PokemonStage.BASIC.value:
        return False
    return "ex" in [name.lower() for name in subtypes_for(pokemon.archetype_id)]


card = PokemonCardDef(
    guid="f60df7ff-8cec-5f37-9ba2-5a1e1686d664",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Farigirafex.Name",
    display_name="Farigiraf ex",
    searchable_by=["Farigiraf ex", "Stage 1", "Tera", "ex", "Farigirafex"],
    subtypes=["Stage 1", "Tera", "ex"],
    collector_number=108,
    set_code="SV5",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    family_id=203,
    abilities=[
        Ability(
            title="Armor Tail",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Basic Pok\u00e9mon ex.",
            passive=prevent_damage_when(
                lambda calc, carrier: calc.target is carrier
                and _is_basic_ex(calc.attacker)),
        ),
        Attack(
            title="Dirty Beam",
            game_text="This attack also does 30 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=unimplemented,
        ),
    ],
)
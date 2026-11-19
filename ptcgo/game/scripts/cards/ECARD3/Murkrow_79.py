from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.attributes import AttrID
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _has_damage(pokemon) -> bool:
    printed = pokemon.attribute_originals.get(AttrID.HP.value)
    return printed is not None and pokemon.get_attribute(AttrID.HP, 0) < printed

card = PokemonCardDef(
    guid="890c5365-cc5f-5bfb-a628-2846764dda62",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    display_name="Murkrow",
    searchable_by=["Murkrow", "Basic", "Murkrow"],
    subtypes=["Basic"],
    collector_number=79,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=198,
    abilities=[
        Attack(
            title="Evil Eye",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. Put a damage counter on that Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Blindside",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has a damage counter on it. This attack does 20 damage to that Pok\u00e9mon. Don't apply Weakness and Resistance.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(20, pool=_has_damage, apply_modifiers=False),
        ),
    ],
)

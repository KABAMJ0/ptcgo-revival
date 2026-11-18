from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from ptcgo.game.card_effects.attacks_common import snipe_attack, damage_per, count_in_play


def _is_damaged(pokemon):
    maximum = pokemon.attribute_originals.get(
        AttrID.HP.value, pokemon.get_attribute(AttrID.HP, 0))
    return pokemon.get_attribute(AttrID.HP, 0) < maximum

card = PokemonCardDef(
    guid="c144199a-8426-52a9-b940-7fc41a93b7ce",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Stunfisk.Name",
    display_name="Stunfisk",
    searchable_by=["Stunfisk", "Basic", "Stunfisk"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SM10",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=618,
    abilities=[
        Attack(
            title="Raging Thunder",
            game_text="This attack does 10 damage to 1 of your Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=snipe_attack(10, pool="bench", count=1, side="mine", also_base=True),
        ),
        Attack(
            title="Electric Trap",
            game_text="This attack does 30 damage for each of your Pok\u00e9mon that has any damage counters on it.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=damage_per(count_in_play("mine", _is_damaged), 30),
        ),
    ],
)
from ptcgo.game.card_effects.attacks_common import damage_per, spread_damage
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session import passives


def _magikarp_counters(ctx):
    """Damage counters on every Magikarp the player has in play."""
    total = 0
    for pokemon in ctx.my_pokemon_in_play():
        if pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) != "Magikarp":
            continue
        total += (passives.effective_max_hp(ctx.board, pokemon)
                  - pokemon.get_attribute(AttrID.HP, 0)) // 10
    return total

card = PokemonCardDef(
    guid="c41dcff2-60a6-5e27-b768-c709bef767e0",
    key="EX8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name",
    display_name="Gyarados",
    searchable_by=["Gyarados", "Stage 1", "Gyarados"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="EX8",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    family_id=129,
    abilities=[
        Attack(
            title="Dragon Spark",
            game_text="This attack does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 1},
            effect=spread_damage(10, side="opponent"),
        ),
        Attack(
            title="Full Retaliation",
            game_text="Does 20 damage times the number of damage counters on all of your Magikarp.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(_magikarp_counters, 20),
        ),
        Attack(
            title="Pulverize",
            game_text="If the Defending Pok\u00e9mon already has at least 2 damage counters on it, this attack does 50 damage plus 50 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
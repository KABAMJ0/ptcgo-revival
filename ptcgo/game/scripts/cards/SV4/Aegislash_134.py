from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, subtypes_for
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.passives_common import prevent_damage_when
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

def _is_ex_or_v(pokemon) -> bool:
    if pokemon is None:
        return False
    subtypes = [name.lower() for name in subtypes_for(pokemon.archetype_id)]
    return "ex" in subtypes or "v" in subtypes


card = PokemonCardDef(
    guid="6deb9f03-cba6-55ff-a2a8-fe09da8afb85",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aegislash.Name",
    display_name="Aegislash",
    searchable_by=["Aegislash", "Stage 2", "Aegislash"],
    subtypes=["Stage 2"],
    collector_number=134,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Doublade.Name",
    family_id=679,
    abilities=[
        Ability(
            title="Mysterious Shield",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon ex and Pok\u00e9mon V.",
            passive=prevent_damage_when(
                lambda calc, carrier: calc.target is carrier
                and _is_ex_or_v(calc.attacker)),
        ),
        Attack(
            title="Hard Bashing",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)
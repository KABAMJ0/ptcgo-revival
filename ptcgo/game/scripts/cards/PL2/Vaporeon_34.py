from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

card = PokemonCardDef(
    guid="aa0cabad-6190-5043-8603-128628c4642a",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name",
    display_name="Vaporeon",
    searchable_by=["Vaporeon", "Stage 1", "Vaporeon"],
    subtypes=["Stage 1"],
    collector_number=34,
    set_code="PL2",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Undevelop",
            game_text="Once during your turn (before your attack), you may devolve Vaporeon and put Vaporeon into your hand. This power can't be used if Vaporeon is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Muddy Water",
            game_text="Does 10 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=snipe_attack(10, pool="bench", count=1, apply_modifiers=False),
        ),
        Attack(
            title="Evolving Aqua",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has any damage counters on it. This attack does 40 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) If Vaporeon evolved from Eevee during this turn, this attack does 60 damage instead.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)
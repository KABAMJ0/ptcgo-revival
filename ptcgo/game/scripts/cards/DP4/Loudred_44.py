from ptcgo.game.card_effects.attacks_common import flip_damage, flip_gate, snipe_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6682488c-484e-5ef3-8cd2-06b80830087b",
    key="DP4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name",
    display_name="Loudred",
    searchable_by=["Loudred", "Stage 1", "Loudred"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="DP4",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Whismur.Name",
    family_id=293,
    abilities=[
        Attack(
            title="Bass Control",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 20 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(20, pool="any"),
        ),
        Attack(
            title="Stomp",
            game_text="Flip a coin. If heads, this attack does 40 damage plus 20 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=flip_gate(then=lambda ctx: ctx.deal_damage(60)),
        ),
    ],
)
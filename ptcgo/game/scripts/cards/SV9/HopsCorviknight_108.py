from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import protect_next_turn
from ptcgo.game.card_effects.attacks_common import snipe_attack
from ptcgo.game.card_effects.passives_common import flip_prevent_damage_passive
card = PokemonCardDef(
    guid="fa010c26-0ee4-5606-ba04-4084a28a7bb4",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCorviknight.Name",
    display_name="Hop's Corviknight",
    searchable_by=["Hop's Corviknight", "Stage 2", "HopsCorviknight"],
    subtypes=["Stage 2"],
    collector_number=108,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.HopsCorvisquire.Name",
    family_id=821,
    abilities=[
        Attack(
            title="Shoot Through",
            game_text="This attack also does 50 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=snipe_attack(50, pool="bench", count=1, apply_modifiers=False, also_base=True),
        ),
        Attack(
            title="Steel Wing",
            game_text="During your opponent's next turn, this Pok\u00e9mon takes 60 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=150,
            effect=protect_next_turn(reduce=60),
        ),
    ],
)
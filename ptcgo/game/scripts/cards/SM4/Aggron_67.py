from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_per, ignore_modifier_attack


def _benched_damage_counters(ctx) -> int:
    """Damage counters on all of your Benched Pokemon."""
    return sum(max(0, (ctx.max_hp(p) - p.get_attribute(AttrID.HP, 0)) // 10)
               for p in ctx.my_bench())


card = PokemonCardDef(
    guid="477b02d8-07c0-523f-b8c9-029ae467e0b8",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron", "Stage 2", "Aggron"],
    subtypes=["Stage 2"],
    collector_number=67,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Revenge Cannon",
            game_text="This attack does 10 more damage for each damage counter on all of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(_benched_damage_counters, 10, base=10),
        ),
        Attack(
            title="Buster Swing",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)
from ptcgo.game.content.definitions import evolves_from
from ptcgo.game.card_effects.passives_common import team_hp_bonus
from ptcgo.game.card_effects.pokemon import is_energy_card
from ptcgo.game.card_effects.support_common import move_energy_between


def _eevee_evolution(pokemon, carrier) -> bool:
    """Your Pokemon that evolve from Eevee."""
    if pokemon is None or carrier is None:
        return False
    if pokemon.owning_player_id != getattr(carrier, "owning_player_id", None):
        return False
    return evolves_from(pokemon.archetype_id, "Eevee")
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def morning_sun(ctx):
    """60, then one Energy off Espeon onto a Benched Pokemon."""
    await ctx.deal_damage(60)
    await move_energy_between(is_energy_card, count=1, from_pool="active",
                              to_pool="bench")(ctx)

card = PokemonCardDef(
    guid="0a58cb61-8572-58d1-8145-f52661eda2fd",
    key="DP5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Espeon.Name",
    display_name="Espeon",
    searchable_by=["Espeon", "Stage 1", "Espeon"],
    subtypes=["Stage 1"],
    collector_number=18,
    set_code="DP5",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Sunlight Veil",
            game_text="Each of your Pok\u00e9mon that evolves from Eevee gets +20 HP. You can't use more than 1 Sunlight Veil Pok\u00e9-Body each turn.",
            passive=team_hp_bonus(20, protects="team",
                                  pred=_eevee_evolution,
                                  stacking_key="Sunlight Veil"),
        ),
        Attack(
            title="Morning Sun",
            game_text="You may move an Energy card attached to Espeon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=morning_sun,
        ),
    ],
)
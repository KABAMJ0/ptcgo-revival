from ptcgo.game.card_effects.attacks_common import lock_opponent_plays
from ptcgo.game.attributes import AttrID
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.attributes import SpecialConditions
from ptcgo.game.data_utils import Triggers
from ptcgo.game.card_effects.pokemon import energy_provides_type


async def _energy_reaction(ctx):
    """Energy Reaction: Grass on attach Asleep, Psychic on attach Poisoned."""
    energy = ctx.attached_energy
    defender = ctx.defender
    if energy is None or defender is None or ctx.effects_blocked(defender):
        return
    if energy_provides_type(energy, PokemonTypes.GRASS.value):
        await ctx.apply_special_condition(defender, SpecialConditions.ASLEEP)
    elif energy_provides_type(energy, PokemonTypes.PSYCHIC.value):
        await ctx.apply_special_condition(defender, SpecialConditions.POISONED)

card = PokemonCardDef(
    guid="4661bca6-364d-579d-8c3b-108dea4f541a",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=45,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Energy Reaction",
            game_text="Once during your turn (before your attack), when you attach a Grass or Psychic Energy card from your hand to Vileplume (excluding effects of attacks or Pok\u00e9-Powers), you may use this power. If you attach a Grass Energy card, the Defending Pok\u00e9mon is now Asleep. If you attach a Psychic Energy card, the Defending Pok\u00e9mon is now Poisoned. This power can't be used if Vileplume is affected by a Special Condition.",
            trigger=Triggers.ON_ENERGY_ATTACHED,
            condition=lambda board, player_id, pokemon: not pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS),
            effect=_energy_reaction,
        ),
        Attack(
            title="Disturbing Pollen",
            game_text="Flip a coin. If heads, your opponent can't play any Trainer, Supporter, or Stadium cards from his or her hand during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=lock_opponent_plays("trainer", "supporter", "stadium", flip=True),
        ),
    ],
)
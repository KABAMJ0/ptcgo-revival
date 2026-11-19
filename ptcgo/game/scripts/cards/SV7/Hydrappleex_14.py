from ptcgo.game.data_utils import Ability, Activations, Attack, PokemonCardDef
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per
from ptcgo.game.card_effects.support_common import attach_from_hand, hand_attach_condition
from ptcgo.game.card_effects.trainers import basic_energy_of

async def _heal_attached(ctx, attached):
    """Ripening Charge's rider: heal 30 from the Pokemon the Energy landed on."""
    for _card, pokemon in attached:
        await ctx.heal(30, pokemon)

card = PokemonCardDef(
    guid="4aac6eeb-6e65-5cfe-a1a1-d779f10c79e5",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydrappleex.Name",
    display_name="Hydrapple ex",
    searchable_by=["Hydrapple ex", "Stage 2", "ex", "Hydrappleex"],
    subtypes=["Stage 2", "ex"],
    collector_number=14,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dipplin.Name",
    family_id=840,
    abilities=[
        Ability(
            title="Ripening Charge",
            game_text="Once during your turn, you may attach a Basic Grass Energy card from your hand to 1 of your Pok\u00e9mon. If you attached Energy to a Pok\u00e9mon in this way, heal 30 damage from that Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=hand_attach_condition(basic_energy_of("grass")),
            effect=attach_from_hand(basic_energy_of("grass"), count=1, target="choice", then=_heal_attached),
        ),
        Attack(
            title="Syrup Storm",
            game_text="This attack does 30 more damage for each Grass Energy attached to all of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=damage_per(count_energy("mine", PokemonTypes.GRASS), per=30, base=30),
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.card_effects.support_common import attach_from_hand, hand_attach_condition
from ptcgo.game.card_effects.trainers import basic_energy_of, card_named_any

async def _electric_streamer(ctx):
    """Attach a Basic Lightning Energy from hand to 1 of your Iono's Pokemon."""
    await attach_from_hand(
        basic_energy_of("lightning"), count=1, target="choice",
        target_pred=card_named_any(["Iono's"]), minimum=1,
        prompt="Choose a Basic Lightning Energy to attach",
    )(ctx)

card = PokemonCardDef(
    guid="86d003d0-05d6-5ba4-a7ee-98a2bee36aa3",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosBelliboltex.Name",
    display_name="Iono's Bellibolt ex",
    searchable_by=["Iono's Bellibolt ex", "Stage 1", "ex", "IonosBelliboltex"],
    subtypes=["Stage 1", "ex"],
    collector_number=183,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosTadbulb.Name",
    family_id=938,
    abilities=[
        Ability(
            title="Electric Streamer",
            game_text="As often as you like during your turn, you may attach a Basic Lightning Energy card from your hand to 1 of your Iono's Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=hand_attach_condition(basic_energy_of("lightning"),
                                            target="choice",
                                            target_pred=card_named_any(["Iono's"])),
            effect=_electric_streamer,
        ),
        Attack(
            title="Thunderous Bolt",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.LIGHTNING: 3, PokemonTypes.COLORLESS: 1},
            damage=230,
            effect=lock_self_attack(),
        ),
    ],
)
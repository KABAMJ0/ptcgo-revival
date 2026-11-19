from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import look_top_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.passives_common import unafflicted

card = PokemonCardDef(
    guid="a3e91ad8-e151-5235-8c74-ea10cdc5fa20",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tyranitar.Name",
    display_name="Tyranitar δ",
    searchable_by=["Tyranitar \u03b4", "Stage 2", "Tyranitar"],
    subtypes=["Stage 2"],
    collector_number=16,
    set_code="EX11",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.FIRE, PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name",
    family_id=248,
    abilities=[
        Ability(
            title="Crush Draw",
            game_text="Once during your turn (before your attack), you may reveal the top card of your deck. If that card is a basic Energy card, attach it to 1 of your Pok\u00e9mon. If not, put the card back on top of your deck. This power can't be used if Tyranitar is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=look_top_attach_energy(1, predicate=is_basic_energy_card,
                                          rest="back"),
        ),
        Attack(
            title="Delta Crush",
            game_text="You may discard an Energy card attached to Tyranitar. If you do, this attack does 50 damage plus 20 more damage.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
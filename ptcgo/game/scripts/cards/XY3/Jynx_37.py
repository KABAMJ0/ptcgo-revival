from ptcgo.game.card_effects.attacks_common import no_retreat_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import heal_activation
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

_heal, _heal_condition = heal_activation(10, requires_benched=True)


card = PokemonCardDef(
    guid="f22c959e-8838-5686-91b2-d04bebe8b037",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name",
    display_name="Jynx",
    searchable_by=["Jynx", "Basic", "Jynx"],
    subtypes=["Basic"],
    collector_number=37,
    set_code="XY3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=124,
    abilities=[
        Ability(
            title="Victory Kiss",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is on your Bench, you may heal 10 damage from your Active Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=_heal,
            condition=_heal_condition,
        ),
        Attack(
            title="Hug",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=no_retreat_attack(),
        ),
    ],
)
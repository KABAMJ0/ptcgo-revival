from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="2efa4f06-da6e-5f4e-aaa6-6e527542404f",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DrapionLVX.Name",
    display_name="Drapion LV.X",
    searchable_by=["Drapion LV.X", "Level-Up", "DrapionLVX"],
    subtypes=["Level-Up"],
    collector_number=123,
    set_code="PL1",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name",
    family_id=452,
    abilities=[
        Ability(
            title="Tri-Poison",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, choose 1 of the Defending Pok\u00e9mon. That Pok\u00e9mon is now Poisoned. Put 3 damage counters instead of 1 on that Pok\u00e9mon between turns. This power can't be used if Drapion is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, mon: not mon.get_attribute(AttrID.SPECIAL_CONDITIONS),
            effect=condition_attack(SpecialConditions.POISONED, flip=True, counters=3),
        ),
        Attack(
            title="Sniping Tail",
            game_text="Does 40 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.) The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from ptcgo.game.card_effects.attacks_common import condition_attack, no_retreat_attack

card = PokemonCardDef(
    guid="9bd5a016-f4e2-541e-8df4-115c57935001",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoom.Name",
    display_name="Houndoom",
    searchable_by=["Houndoom", "Stage 1", "Prime", "Houndoom"],
    subtypes=["Stage 1", "Prime"],
    collector_number=82,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=228,
    abilities=[
        Ability(
            title="Fire Breath",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, the Defending Pok\u00e9mon is now Burned. This power can't be used if Houndoom is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, mon: not mon.get_attribute(AttrID.SPECIAL_CONDITIONS),
            effect=condition_attack(SpecialConditions.BURNED, flip=True),
        ),
        Attack(
            title="Dark Clamp",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=no_retreat_attack(),
        ),
    ],
)
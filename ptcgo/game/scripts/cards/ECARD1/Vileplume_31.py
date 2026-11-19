from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions, AttrID
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="55f4025f-c55d-562f-8251-352dc04e0ab9",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vileplume.Name",
    display_name="Vileplume",
    searchable_by=["Vileplume", "Stage 2", "Vileplume"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="ECARD1",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    family_id=43,
    abilities=[
        Ability(
            title="Poison Pollen",
            game_text="Once during your turn (before your attack), you may flip a coin. If heads, the Defending Pok\u00e9mon is now Poisoned. This power can't be used if Vileplume is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=lambda board, player_id, mon: not mon.get_attribute(AttrID.SPECIAL_CONDITIONS),
            effect=condition_attack(SpecialConditions.POISONED, flip=True),
        ),
        Attack(
            title="Petal Dance",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads. Vileplume is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
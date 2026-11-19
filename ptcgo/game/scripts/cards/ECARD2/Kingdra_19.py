from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6f0bf7dc-c77d-5969-8c06-bf95aa91e780",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kingdra.Name",
    display_name="Kingdra",
    searchable_by=["Kingdra", "Stage 2", "Kingdra"],
    subtypes=["Stage 2"],
    collector_number=19,
    set_code="ECARD2",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name",
    family_id=116,
    abilities=[
        Ability(
            title="Water Cyclone",
            game_text="As often as you like during your turn (before your attack), you may move a Water Energy card from your Active Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. This power can't be used if Kingdra is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Rapids",
            game_text="Flip a coin. If heads, discard 1 Energy card attached to the Defending Pok\u00e9mon, if any.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=discard_opponent_energy_attack(count=1, flip=True),
        ),
    ],
)
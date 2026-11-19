from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import energy_move_attack

card = PokemonCardDef(
    guid="691686e1-2b70-5c7d-b983-82fe789cdcf4",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name",
    display_name="Togekiss",
    searchable_by=["Togekiss", "Stage 2", "Togekiss"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name",
    family_id=468,
    abilities=[
        Ability(
            title="Precious Gift",
            game_text="Once at the end of your turn (after your attack), you may use this Ability. Draw cards until you have 8 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Power Cyclone",
            game_text="Move an Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=110,
            effect=energy_move_attack(count=1),
        ),
    ],
)
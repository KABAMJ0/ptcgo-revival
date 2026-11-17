from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="38ab1fe2-3f7c-59da-98d1-5efb36f96641",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Flareon.Name",
    display_name="Flareon",
    searchable_by=["Flareon", "Stage 1", "Flareon"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="ECARD3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Self-healing",
            game_text="Whenever you attach a Fire Energy card from your hand to Flareon, remove all Special Conditions affecting Flareon.",
            effect=unimplemented,
        ),
        Attack(
            title="Singe",
            game_text="The Defending Pok\u00e9mon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Burn Booster",
            game_text="Discard an Energy card attached to Flareon in order to use this attack. If the discarded card is a Fire Energy card, this attack does 40 damage plus 10 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)
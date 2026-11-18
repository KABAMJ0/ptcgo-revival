from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="81790a43-d72f-5278-95b4-09f3bdfdc187",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Revavroom.Name",
    display_name="Revavroom",
    searchable_by=["Revavroom", "Stage 1", "Revavroom"],
    subtypes=["Stage 1"],
    collector_number=65,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Varoom.Name",
    family_id=965,
    abilities=[
        Ability(
            title="Rumbling Engine",
            game_text="You must discard an Energy card from your hand in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Knock Away",
            game_text="Flip a coin. If heads, this attack does 90 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator="+",
            effect=flip_bonus(90),
        ),
    ],
)
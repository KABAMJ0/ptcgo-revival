from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="72e9e3cd-5255-5fde-bd7c-a0d6eaf87775",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Starmie.Name",
    display_name="Starmie",
    searchable_by=["Starmie", "Stage 1", "Starmie"],
    subtypes=["Stage 1"],
    collector_number=50,
    set_code="PL2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    family_id=120,
    abilities=[
        Ability(
            title="Aqua Recycle",
            game_text="Once during your turn (before your attack), you may search your discard pile for a Water Energy card, show it to your opponent, and put it into your hand. This power can't be used if Starmie is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Synchro Gain",
            game_text="If Starmie and the Defending Pok\u00e9mon have the same amount of Energy attached to them, remove 4 damage counters from Starmie.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Powerful Spin",
            game_text="Starmie can't attack during your next turn.",
            cost={PokemonTypes.WATER: 1},
            damage=40,
            effect=unimplemented,
        ),
    ],
)
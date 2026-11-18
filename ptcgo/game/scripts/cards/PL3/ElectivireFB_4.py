from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fdb52ea2-31a5-5089-ac45-396c27f47775",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ElectivireFB.Name",
    display_name="Electivire FB",
    searchable_by=["Electivire FB", "Basic", "SP", "ElectivireFB"],
    subtypes=["Basic", "SP"],
    collector_number=4,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    family_id=466,
    abilities=[
        Attack(
            title="Dump and Draw",
            game_text="Discard up to 2 Energy cards from your hand. For each card you discarded, draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Electric Current",
            game_text="Move a Lightning Energy card attached to Electivire FB to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)
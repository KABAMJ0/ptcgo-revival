from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a8ba95de-1912-51b9-a36a-01e2c0c10926",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansMagcargo.Name",
    display_name="Ethan's Magcargo",
    searchable_by=["Ethan's Magcargo", "Stage 1", "EthansMagcargo"],
    subtypes=["Stage 1"],
    collector_number=222,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.EthansSlugma.Name",
    family_id=218,
    abilities=[
        Ability(
            title="Melt Away",
            game_text="If this Pok\u00e9mon has no Energy attached, it has no Retreat Cost.",
            effect=unimplemented,
        ),
        Attack(
            title="Lava Burst",
            game_text="Discard up to 5 Fire Energy from this Pok\u00e9mon. This attack does 70 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIRE: 3},
            damage=70,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
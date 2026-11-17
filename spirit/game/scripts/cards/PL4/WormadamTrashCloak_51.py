from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b52f9267-fb90-588a-9ac4-8f1b652d169b",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WormadamTrashCloak.Name",
    display_name="Wormadam Trash Cloak",
    searchable_by=["Wormadam Trash Cloak", "Stage 1", "WormadamTrashCloak"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="PL4",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.BurmyTrashCloak.Name",
    family_id=412,
    abilities=[
        Attack(
            title="Cloak Shard",
            game_text="Choose 1 of your opponent's Pok\u00e9mon. This attack does 10 damage to that Pok\u00e9mon. If you have Wormadam Plant Cloak in play, this attack does 40 damage to that Pok\u00e9mon instead. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Serve Trash",
            game_text="You may search your opponent's discard pile for any 1 card, show it to your opponent, and put it on top of his or her deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2b5c6ee5-14e8-5e32-a594-4f83f17d7314",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Groudon.Name",
    display_name="Groudon",
    searchable_by=["Groudon", "Basic", "Groudon"],
    subtypes=["Basic"],
    collector_number=199,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=383,
    abilities=[
        Attack(
            title="Swelling Power",
            game_text="Attach a Basic Fighting Energy card from your hand to 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Magma Purge",
            game_text="Discard up to 4 Energy from your Pok\u00e9mon. This attack does 60 damage for each card you discarded in this way.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)
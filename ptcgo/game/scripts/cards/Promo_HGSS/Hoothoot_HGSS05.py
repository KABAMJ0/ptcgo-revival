from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7abc8a3d-aba6-5abf-8fb6-a4939b4686d0",
    key="Promo_HGSS",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name",
    display_name="Hoothoot",
    searchable_by=["Hoothoot", "Basic", "Hoothoot"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="Promo_HGSS",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=163,
    abilities=[
        Ability(
            title="Insomnia",
            game_text="Hoothoot can't be Asleep.",
            effect=unimplemented,
        ),
        Attack(
            title="Peck",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a7921108-dc5d-545a-8d3b-d63b3adc1198",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoGX.Name",
    display_name="Solgaleo-GX",
    searchable_by=["Solgaleo-GX", "Stage 2", "GX", "SolgaleoGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=104,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=791,
    abilities=[
        Ability(
            title="Shining Mane",
            game_text="Your Pok\u00e9mon in play have no Weakness.",
            effect=unimplemented,
        ),
        Attack(
            title="Turbo Strike",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
        Attack(
            title="Prominence-GX",
            game_text="Heal all damage from all of your Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)
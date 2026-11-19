from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_all_from_one

card = PokemonCardDef(
    guid="5330b0a7-73f4-52e0-9b22-9ce5c68e3156",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Primarina.Name",
    display_name="Primarina",
    searchable_by=["Primarina", "Stage 2", "Primarina"],
    subtypes=["Stage 2"],
    collector_number=20,
    set_code="ME5",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    family_id=728,
    abilities=[
        Ability(
            title="Enriching Melody",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. Heal all damage from 1 of your Pok\u00e9mon.",
            trigger=Triggers.ON_EVOLVE,
            effect=heal_all_from_one(),
        ),
        Attack(
            title="Aqua Return",
            game_text="Shuffle this Pok\u00e9mon and all attached cards into your deck.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=unimplemented,
        ),
    ],
)
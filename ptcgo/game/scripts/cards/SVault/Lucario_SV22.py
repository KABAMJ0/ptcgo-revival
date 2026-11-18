from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="2f25b7ec-b33c-580f-8ba3-af8feb0e4d49",
    key="SVault",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name",
    display_name="Lucario",
    searchable_by=["Lucario", "Stage 1", "Lucario"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="SVault",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=447,
    abilities=[
        Ability(
            title="Precognitive Aura",
            game_text="Once during your turn (before your attack), if you have Garchomp in play, you may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Missile Jab",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)